a,b=map(int,input().split())

# aをずっと足していくパターン
i1=b-a if a<b else float("inf")

# aをずっと足していき、-aにするパターン
i2=-a-b+1 if -a>=b else float("inf")

# -aにしてずっと足していくパターン
i3=a+b+1 if -a<=b else float("inf")

# -aにしてずっと足して、さらに -aにするパターン
i4=a-b+2 if a>=b else float("inf")


print(min(i1,i2,i3,i4))