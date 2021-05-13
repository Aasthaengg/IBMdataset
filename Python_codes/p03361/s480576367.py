H,W=map(int,input().strip().split())
s=[]
for _ in range(H):
    s.append(list(input()))

def judge(i,j,s,H,W):
    find=False
    dh=[0,1,0,-1]
    dw=[1,0,-1,0]
    for n in range(4):
        if 0<=i+dh[n]<=H-1 and 0<=j+dw[n]<=W-1:
            if s[i+dh[n]][j+dw[n]]=="#":
                find=True
                break
    return find

def main():
    end=False
    for i in range(H):
        if end==True:
            break
        for j in range(W):
            if s[i][j]=="#":
                if not judge(i,j,s,H,W):
                    print("No")
                    end=True
                    break
    if end==False:
        print("Yes")
if __name__=="__main__":
	main()