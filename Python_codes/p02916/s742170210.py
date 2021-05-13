n = int(input())
# mapはcallable, iterator
# input().split()でリストを作成する
a = [int(i) for i in input().split()]
iSSequence = [False] * (len(a) - 1)

# a[i]のあとにa[i+1]を食べたならフラグを立てる
for i in range(len(a) - 1):
    if(a[i] + 1 == a[i + 1]):
        iSSequence[a[i] - 1] = True

sum = 0
# bは必ずすべて足される
for b in input().split():
    sum += int(b)

index = 0
for c in input().split():
    if(iSSequence[index]):
        sum += int(c)
    index += 1

print(sum)