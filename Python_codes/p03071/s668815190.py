A,B = list(map(int,input().split()))

coinGainList = []

coinGainList = [A+A-1, B+B-1, A+B]
maxGain = max(coinGainList)
print(maxGain)