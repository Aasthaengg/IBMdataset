print(2**max((i^(i-1)).bit_length()-1 for i in range(int(input())+1)))