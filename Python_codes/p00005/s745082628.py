# -*- coding: utf-8 -*-

while True:
  try:
    ( a, b ) = map ( int, input ( ).split ( ) )
  except EOFError: break
  ( x, y ) = ( a, b )
  while x != 0:
    ( x, y ) = ( y % x, x )
  print ( "%s %s" % ( y, a * b // y ) )