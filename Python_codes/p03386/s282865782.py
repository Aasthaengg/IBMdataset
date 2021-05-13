#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]
#a = [int(input()) for _ in range(n)]

a,b,k=map(int, input().split())

ans = []
for i in range(a,min(b+1,a+k)):
    ans.append(i)
for i in range(b,max(a-1,b-k),-1):
    ans.append(i)
ans = list(set(ans))
ans.sort()
for i in range(len(ans)):
    print(ans[i])




