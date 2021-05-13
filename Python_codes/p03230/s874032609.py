K = int(input())

def calc_n(K):
  for n in range(1, int(K/2)+2):
    if n*(n+1)/2 == K:
      return n
  return "No"

N = calc_n(K)
if not isinstance(N, int):
  print(N)
else:
  print("Yes")
  print(N+1)
  last = [i for i in range(1, N+1)]
  count = 2
  first_set = [str(i) if i == 1 else str(sum(last[:i-1])+1) for i in range(1, N+1)]
  print(N, " ".join(first_set))
  last_set = [str(sum(last[:i])) for i in range(1,N+1)]
  print(N, " ".join(last_set))
  while count != N+1:
    first_number = sum(last[:count-1])+1
    other_set = [i for i in range(first_number, first_number+count)]
    other_set.extend([first_number+count*(i+1)-1+sum(last[:i-1]) for i in range(1, N-count+1)])
    count += 1
    other_set = [str(i) for i in other_set]
    print(N, " ".join(other_set))