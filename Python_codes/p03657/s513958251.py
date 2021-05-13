A, B = map(int, input().split())
if A % 3 == 0:
    s = 'Possible'
elif B % 3 == 0:
    s = 'Possible'
elif (A + B) % 3 == 0:
    s = 'Possible'
else:
    s = 'Impossible'
print(s)