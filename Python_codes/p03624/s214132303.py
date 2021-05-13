S = set(input())
for i in range(ord("a"), ord("z") + 1):
    if not (chr(i) in S):
        print(chr(i))
        break
else:
    print("None")
