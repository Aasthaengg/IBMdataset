s = list(input())
odd = ['R', 'U', 'D']
even = ['L', 'U', 'D']
ret = 'Yes'
for i, j in enumerate(s):
    if (i+1)%2 == 1 and j not in odd:
        ret = 'No'
        break
    elif (i+1)%2 == 0 and j not in even:
        ret = 'No'
        break
print(ret)