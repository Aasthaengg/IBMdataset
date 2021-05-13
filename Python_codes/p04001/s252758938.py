def main():
  # S = list(input())
  S = input()

  sum_ = 0
  for bit in range(1 << len(S)-1):
    pre = 0
    for i in range(len(S)-1):
      mask = 1 << i
      if (bit & mask):
        # print(S[pre:i+1])
        sum_ += int(S[pre:i+1])
        pre = i+1
      # print('bit:', bin(bit))
      # print('mask', bin(mask))
    # print(S[pre:])
    sum_ += int(S[pre:])
  print(sum_)


if(__name__ == '__main__'):
  main()