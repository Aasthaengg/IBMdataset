K = int(input())
odd = 0
even = 0
for i in range(1, K+1):
    if i%2 == 0:
        even += 1
    else:
        odd +=1
print(odd*even)