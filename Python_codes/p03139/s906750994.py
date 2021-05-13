Sample, NumOfPaperA, NumOfPaperB = map(int, input().split())
MaximumNumberOfBothReader = min(NumOfPaperA, NumOfPaperB)
MinimumNumberOfBothReader = max(NumOfPaperA + NumOfPaperB - Sample, 0)
print(str(MaximumNumberOfBothReader) + ' ' + str(MinimumNumberOfBothReader))
