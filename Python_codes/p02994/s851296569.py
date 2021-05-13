n,l=map(int,input().split())
left=l
right=l+n-1
apple=[i for i in range(left,right+1)]
if left<=0<=right:
  print(sum(apple))
elif left<0 and right<0:
  print(sum(apple)-right)
elif 0<left and 0<right:
  print(sum(apple)-left)

