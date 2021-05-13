S = input()
S_set = set(S)

for i in range(97,123):
    if chr(i) not in S_set:
        print(chr(i))
        exit()
print("None")
