ss = list(map(int, input().strip().split()))
total=0
N=ss[0]
X=ss[1]
T=ss[2]

kaisuu = -(-N//X)
createtime=kaisuu * T
print(createtime)