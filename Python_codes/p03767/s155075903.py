n = int(input())
a_inputs = sorted([int(i) for i in input().split()])

k_num = len(a_inputs)
#弱い順にソート,最初のk人を一番弱いメンバーとする。
#残りを(k+1,k+2),(k+3,k+4),...(n-1,n)と並べた時のk+1,k+3...n-1の値値を求める

print(sum([a_inputs[i] for i in range(n,k_num,2)]))