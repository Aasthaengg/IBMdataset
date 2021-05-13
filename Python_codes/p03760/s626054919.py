#B - ∵∴∵ 
O = list(input())
E = list(input())

S = [O[i//2] if i%2 == 0 else E[i//2] for i in range(len(O)+len(E))]
    
print(''.join(S))