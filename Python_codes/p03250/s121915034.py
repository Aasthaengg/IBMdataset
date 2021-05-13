li=list(map(int,input().split()))
ma=max(li)*10
li.remove(max(li))
li.append(ma)
print(sum(li))