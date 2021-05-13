n, m, l = [int(_) for _ in input().split()]

a = []
b = []
for _ in range(n):
  a.append([int(__) for __ in input().split()])

for _ in range(m):
  b.append([int(__) for __ in input().split()])

output_list = []
for ac in a:
  output = []
  for bc in zip(*b):
    output.append(sum([acc*bcc for acc, bcc in zip(ac,bc)]))
  output_list.append(output)

for olist in output_list:
  print(" ".join([str(_) for _ in olist]))