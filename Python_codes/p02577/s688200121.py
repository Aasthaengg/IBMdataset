str = input()
sum = 0
for ch in str:
    sum += ord(ch) - ord('0')
if sum % 9 == 0:
    print("Yes")
else:
    print("No")