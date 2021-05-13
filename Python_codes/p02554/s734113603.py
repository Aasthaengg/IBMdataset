# 21:17-                                                                                                                                                      
N = int(input())

kMod = 10**9+7

print((pow(10, N, kMod) - 2*pow(9, N, kMod)+pow(8, N, kMod) + kMod) % kMod)