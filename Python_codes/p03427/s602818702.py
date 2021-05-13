n = int(input())
if (n//10**(len(str(n))-1)+1)*10**(len(str(n))-1)-1 > n:
  mx = (n//10**(len(str(n))-1))*10**(len(str(n))-1)-1
else:
  mx = (n//10**(len(str(n))-1)+1)*10**(len(str(n))-1)-1
print(sum(list(map(int,str(mx)))))