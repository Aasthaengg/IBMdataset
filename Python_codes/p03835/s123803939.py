import numpy as np
K, S = map(int, input().split())
arrange = np.arange(K + 1)
T = S - np.add.outer(arrange, arrange)
print(((T >= 0) & (T <= K)).sum())