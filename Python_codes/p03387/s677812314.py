A, B, C = sorted(map(int, input().split()))
B, C = B-A, C-A
def calc(x):
  return (x+x%2)//2+x%2 if x>0 else -x
print(min(calc(i)+calc(i-B)+calc(i-C) for i in range(51)))