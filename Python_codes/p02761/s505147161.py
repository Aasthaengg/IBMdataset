import copy
def main():
    n,m = map(int,input().split())
    sc = []
    for i in range(m):
        s,c = map(int,input().split())
        sc.append([s,str(c)])
    if n==1:
        for i in range(10):
            flag = True
            tmp = str(i)
            tmp = list(tmp)
            tmp = ['0' for j in range(n-len(tmp))] + tmp
            for j in range(m):
                if tmp[sc[j][0]-1] !=sc[j][1]:
                    flag = False
            if flag:
                print(i)
                exit()
            
    else:        
        for i in range(10**(n-1),10**n):
            flag = True
            tmp = str(i)
            tmp = list(tmp)
            tmp = ['0' for j in range(n-len(tmp))] + tmp
            
            for j in range(m):
                if tmp[sc[j][0]-1] !=sc[j][1]:
                    flag = False
            if flag:
                print(i)
                exit()
    print('-1')
main()