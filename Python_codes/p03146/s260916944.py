s=int(input())
def f(n):
  if n%2==0:
    return n/2
  else:
    return 3*n+1
  
seq=[0 for i in range(1000000)]
seq[0]=s
seq[1]=f(seq[0])
count =1
set={s,seq[1]}
while 1-(f(seq[count]) in set):
  seq[count+1]=f(seq[count])
  set.add(f(seq[count]))
  count=count+1

print(count+2)