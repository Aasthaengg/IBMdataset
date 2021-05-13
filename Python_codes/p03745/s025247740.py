n=int(input())
a=list(map(int,input().split()))
is_up=False
is_even=True
pre_a=a[0]
cnt=1
for aa in a:
  if is_even and pre_a != aa:
    is_even=False
    is_up=pre_a < aa
  if not is_even:
    if (is_up and pre_a > aa) or (not is_up and pre_a < aa):
      is_even=True
      cnt+=1
  pre_a=aa
print(cnt)