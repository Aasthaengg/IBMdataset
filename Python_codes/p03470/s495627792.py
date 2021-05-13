I = int(input())
L = []
for i in range(I):
    L.append(int(input()))

def unique(collection):
    result = []
    return [x for x in collection if x not in result and not result.append(x)]

print(len(unique(L)), flush=True)
