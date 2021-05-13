try:
   while True:
      cards = input()
      if cards == "-": break
      m = int(input()) #シャッフルの回数
      
      for i in range(m):
         h = int(input()) #シャッフルするカードの枚数
         neworder = cards[h:len(cards)]
         #print("#1", neworder)
         for j in range(h):
            #print("+", cards[j])
            neworder += cards[j]
            #print("#", neworder)
         cards = neworder
         #print("#2", cards)
   
      print(cards)

except EOFError:
   pass

