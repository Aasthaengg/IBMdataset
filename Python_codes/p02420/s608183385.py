def process(alpha, m):
    for i in range(m):
        h = int(input())
        ba = alpha[:h]
        #print(ba)
        alpha = alpha[h:] + ba
        #print(alpha)
    return alpha

results = []

while True:
    alpha = input()
    if alpha == "-":
        break
    m = int(input())
    res = process(alpha, m)
    results.append(res)

for w in results:
    print(w)
