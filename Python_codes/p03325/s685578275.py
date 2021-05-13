N = int(input())
a = list(map(int,input().split()))

def divide_two(x,c=0):
  if x % 2 == 1:
    return c
  else:
    return divide_two(x//2,c+1)

b = (divide_two(x) for x in a)

print(sum(list(b)))