def DivisorsTable(N):
    DivTable = [0]*(N+1) 
    for I in range(1,N+1):
        for J in range(I,N+1,I):
            DivTable[J] += 1
    return sum(DivTable)
print(DivisorsTable(int(input())-1))