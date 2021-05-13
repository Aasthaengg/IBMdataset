n=list(map(int, input().split()))
ans=0
diff=n[1]-n[0]
for i in range(diff):
  ans=i+ans
yuki=ans-n[0]
print(yuki)