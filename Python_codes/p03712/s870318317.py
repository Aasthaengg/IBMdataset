h,w = map(int, input().split())
a = ['#'+input().strip()+'#' for _ in range(h)]
print('#' * (w+2))
print('\n'.join(a))
print('#' * (w+2))