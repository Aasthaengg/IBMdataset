def warimakuri(num):
  return format(num, 'b')[::-1].find('1')
N=int(input())
L=list(map(int,input().split()))
L=[warimakuri(i) for i in L]
print(min(L))