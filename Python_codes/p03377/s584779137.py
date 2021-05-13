cat_num, animal_num, just = map(int, input().split())
print("YES" if just>=cat_num and just<=cat_num+animal_num else "NO")