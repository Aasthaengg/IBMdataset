N=int(input())
cnt=len(list(filter(lambda a:a%2==1, map(int,input().split()))))

if cnt%2==0:
    print("YES")
else:
    print("NO")
