O=input()
E=input()

ans = [O[i//2] if i % 2 == 0 else E[i//2] for i in range(len(O)+len(E))]
print(''.join(ans))