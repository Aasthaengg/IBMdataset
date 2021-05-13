N = map(int,input().split())
Numbers = list(map(int,input().split()))
if len(set(Numbers))==len(Numbers):
    print("YES")
else :
    print("NO")