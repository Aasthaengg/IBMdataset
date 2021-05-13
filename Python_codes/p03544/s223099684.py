L=int(input())

lyuca=[2,1]
for i in range(2,L+1):
  a=lyuca[i-1]+lyuca[i-2]
  lyuca.append(a)
print(lyuca[-1])
