a,b = raw_input().split()
c = int(a + b)
k = 0
while(k ** 2 < c): k+=1
print 'Yes' if k ** 2 == c else 'No'