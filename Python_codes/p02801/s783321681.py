c = input()
alphs= [chr(ord('a') + i) for i in range(26)]
for i in range(26):
    if c == alphs[i]:
        print(alphs[i+1])
