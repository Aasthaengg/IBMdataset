O = input()
E = input()
num = len(O) + len(E)
ans = [O[i//2] if i % 2 == 0 else E[i//2] for i in range(num)]
print(''.join(ans))
