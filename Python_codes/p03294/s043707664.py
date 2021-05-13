N=int(input())

a_list = list(map(int,input().split()))

# a1, a2, a3..で割られた際一番余りの大きい数はそれぞれ a1-1, a2-1, a3-1..なのでそれらの合計が答え

print(sum(a_list)-N)
