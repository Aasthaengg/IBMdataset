InData=input().split()
InDataM = [int(i) for i in InData]
result = sorted(InDataM)
print(' '.join(map(str, result)))
