N = int(input())
odd = []
even = []
four = []
for x in map(int,input().split()):
    if x % 4 == 0:
        four.append(x)
    elif x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)
if len(four) >= len(odd):
    print("Yes")
elif len(four) == len(odd)-1 and len(even) == 0:
    print("Yes")
else:
    print("No")