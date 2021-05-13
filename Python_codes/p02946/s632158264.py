import numpy as np
K, X = map(int, input().split())

ans = [str(x) for x in range(X-K+1,X+K)]
ans = " ".join(ans)
print(ans)