# CODE FESTIVAL 2017 予選 C: B – Similar Arrays
N = int(input())
A = [int(i) for i in input().split()]

num_even = len([i for i in A if i % 2 == 0])
print(3 ** N - 2 ** num_even)