def main():
    h,w,k = map(int,input().split())
    g = []
    for _ in range(h):
        g.append(input())
    
    ans = 0
    for hb in range(0b1<<h):
        for wb in range(0b1<<w):
            temp = 0
            for i in range(h):
                for j in range(w):
                    if 0b1&hb>>i and 0b1&wb>>j:
                        if g[i][j] == "#":
                            temp+=1
            
            if temp==k:
                ans+=1
    
    print(ans)
main()