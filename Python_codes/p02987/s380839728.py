import collections
moji=sorted(list(input()))
if moji[0]==moji[1] and moji[2]==moji[3] and moji[0] != moji[2]:
    print("Yes")
else:
    print("No")