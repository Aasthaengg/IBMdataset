def ni(num):
  return format(num, 'b')[::-1].find('1')
N=int(input())
L=list(map(int,input().split()))
L=list(map(ni,L))
print(sum(L))