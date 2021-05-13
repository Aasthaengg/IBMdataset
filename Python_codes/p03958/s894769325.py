#3問目 CODE FESTIVAL 2016 qual C B問題 -K個のケーキ
KT = map(int, input().split())
A = [int(s) for s in input().split()]
Max_i = 0
Max = 0
withoutMaxSum = 0
#二回連続で食べる可能性のあるケーキは一番個数の多いケーキのみ
#一番個数の多いケーキの個数 - その他のケーキの個数の総和 - 1が前日と同じケーキを食べる日数
#0以下になったら確実に被らずに食べられる
#1以上になったら確実に被る -> max(0, Max - withoutMaxSum)
for i in range(len(A)):
    if(Max < A[i]):
        Max = A[i]
        Max_i = i
for i in range(len(A)):
    if(i != Max_i):
        withoutMaxSum += A[i]
print(max(0, Max-withoutMaxSum-1))