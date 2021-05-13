n,c,k = map(int,input().split())
t = [int(input()) for _ in range(n)]
t.sort()
cnt = 0
ans = 0
end = -1
for i,t in enumerate(t):
  if end < t:
    cnt = 1
    ans +=1
    end = t+k
  else:
    cnt +=1
  if cnt > c:
    cnt = 1
    ans +=1
    end = t+k
#  print("i",i,"t",t,"cnt",cnt,"ans",ans,"end",end)
print(ans)